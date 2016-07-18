
import unittest

import jsonschema
import yaml


class SchemaTests(unittest.TestCase):

    with open('schema.yaml') as file:
        validator = jsonschema.Draft4Validator(yaml.safe_load(file))

    def test_valid(self):
        with open('fixtures/valid.json') as file:
            self.validator.validate(yaml.safe_load(file))

    def test_invalid(self):
        # Missing end dates from 'general election'-class events
        with open('fixtures/invalid.json') as file, \
                self.assertRaises(jsonschema.exceptions.ValidationError):
            self.validator.validate(yaml.safe_load(file))


if __name__ == '__main__':
    unittest.main()
