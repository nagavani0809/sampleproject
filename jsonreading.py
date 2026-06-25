import json
from json import JSONDecodeError


def testcount():
    try:
        data = json.load(open('C:/Users/Prapul/Downloads/sample_test_results.json'))


    except FileNotFoundError:
        raise FileNotFoundError("C:/Users/Prapul/Downloads/sample_test_results.json")
    except JSONDecodeError as err:
        raise err

    passed=0
    failed=0

    for test_case in data.get("test_cases","[]"):
        if test_case.get("status","").upper() == "PASS":
            passed+=1
        else:
            failed+=1

    return passed, failed

if __name__ == "__main__":
    passed, failed = testcount()
    print(f"Passed: {passed}, Failed: {failed}")


