import pathlib
import unittest


class SetupMetadataTest(unittest.TestCase):
    def test_required_runtime_dependencies_are_declared(self):
        setup_path = pathlib.Path(__file__).resolve().parents[1] / "setup.py"
        setup_source = setup_path.read_text(encoding="utf-8")

        self.assertIn('"beautifulsoup4"', setup_source)
        self.assertIn('"requests"', setup_source)


if __name__ == "__main__":
    unittest.main()
