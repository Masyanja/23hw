import functions

CMD_TO_FUNCTION = {
    'filter': functions.filter_query,
    'map': functions.map_query,
    'unique': functions.unique_query,
    'sort': functions.sort_query,
    'limit': functions.limit_query
}

FILE_NAME = 'data/apache_logs.txt'


def build_query(cmd, param):
    with open(FILE_NAME) as file:
        prepared_data = list(map(lambda x: x.strip(), file))

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)


def build_query_2(cmd, param, res_data):
    return CMD_TO_FUNCTION[cmd](param=param, data=res_data)
