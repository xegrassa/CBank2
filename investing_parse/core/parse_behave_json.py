from investing_parse.core.help_function import get_data_json
from typing import List


def _get_scenario_name(json) -> str:
    return json['name']


def _get_scenario_status(json) -> str:
    return json['status']


def _get_steps_count(json) -> str:
    return str(len(json['steps']))


def _get_passed_time(json) -> str:
    """Return time sum, all steps"""
    time = 0
    for step in json['steps']:
        try:
            time += float(step['result']['duration'])
        except KeyError:
            break
    return '{}m {:2.3f}s'.format(int(time // 60), time % 60)


def parse_behave_json_report(path: str) -> List[dict]:
    """Return data from behave report"""
    f = get_data_json(path)
    scenario_report = []
    for scenario in f[0]['elements']:
        scenario_report.append({'name': _get_scenario_name(scenario),
                                      'status': _get_scenario_status(scenario),
                                      'steps_count': _get_steps_count(scenario),
                                      'time': _get_passed_time(scenario)
                                })
    return scenario_report
