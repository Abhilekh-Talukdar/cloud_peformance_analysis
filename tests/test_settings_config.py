import unittest

from api.config import (
    get_allowed_hosts,
    get_bool_setting,
    get_secret_key,
    get_sqlite_database_path,
)


class SettingsConfigurationTests(unittest.TestCase):
    def test_secret_key_is_required_and_trimmed(self):
        with self.assertRaisesRegex(RuntimeError, "DJANGO_SECRET_KEY"):
            get_secret_key({})
        self.assertEqual(
            get_secret_key({"DJANGO_SECRET_KEY": "  generated-secret  "}),
            "generated-secret",
        )

    def test_debug_defaults_to_false(self):
        self.assertFalse(get_bool_setting("DJANGO_DEBUG", default=False, environ={}))

    def test_boolean_setting_accepts_supported_values(self):
        for value in ("1", "true", "YES", "on"):
            with self.subTest(value=value):
                self.assertTrue(
                    get_bool_setting("DJANGO_DEBUG", False, {"DJANGO_DEBUG": value})
                )

        for value in ("0", "false", "NO", "off"):
            with self.subTest(value=value):
                self.assertFalse(
                    get_bool_setting("DJANGO_DEBUG", True, {"DJANGO_DEBUG": value})
                )

    def test_boolean_setting_rejects_ambiguous_values(self):
        with self.assertRaisesRegex(ValueError, "DJANGO_DEBUG"):
            get_bool_setting("DJANGO_DEBUG", False, {"DJANGO_DEBUG": "sometimes"})

    def test_allowed_hosts_default_to_loopback_only(self):
        self.assertEqual(
            get_allowed_hosts({}),
            ["localhost", "127.0.0.1"],
        )

    def test_allowed_hosts_parse_comma_separated_values(self):
        self.assertEqual(
            get_allowed_hosts(
                {"DJANGO_ALLOWED_HOSTS": " api.example.com,localhost "}
            ),
            ["api.example.com", "localhost"],
        )

    def test_allowed_hosts_reject_empty_and_wildcard_values(self):
        for value in ("", " , "):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "hostname"):
                get_allowed_hosts({"DJANGO_ALLOWED_HOSTS": value})

        with self.assertRaisesRegex(ValueError, "wildcard"):
            get_allowed_hosts({"DJANGO_ALLOWED_HOSTS": "*"})

    def test_database_path_defaults_inside_project(self):
        self.assertEqual(
            get_sqlite_database_path("/srv/app", {}),
            "/srv/app/db.sqlite3",
        )

    def test_database_path_supports_absolute_and_relative_overrides(self):
        self.assertEqual(
            get_sqlite_database_path(
                "/srv/app",
                {"DJANGO_SQLITE_PATH": "data/app.sqlite3"},
            ),
            "/srv/app/data/app.sqlite3",
        )
        self.assertEqual(
            get_sqlite_database_path(
                "/srv/app",
                {"DJANGO_SQLITE_PATH": "/var/lib/app.sqlite3"},
            ),
            "/var/lib/app.sqlite3",
        )


if __name__ == "__main__":
    unittest.main()
