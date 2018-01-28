import json
import os


class Common(object):
    RESULT_DIR = 'result'
    PADDYPOWER_SPIDER_NAME = 'paddypower'
    SKYBET_SPIDER_NAME = 'skybet'
    WILLIAM_HILL_SPIDER_NAME = 'williamhill'

    @classmethod
    def write_result(cls, name, result):
        if not os.path.exists(cls.RESULT_DIR):
            os.makedirs(cls.RESULT_DIR)
        file_name = '{}.json'.format(name)
        with open(os.path.join(cls.RESULT_DIR, file_name), 'w') as f:
            json.dump(result, f)

    @classmethod
    def read_result(cls):
        result = {}
        for file in os.listdir(cls.RESULT_DIR):
            with open(os.path.join(cls.RESULT_DIR, file)) as f:
                name = file.split('.')[0]
                result[name] = json.load(f)
        return result
