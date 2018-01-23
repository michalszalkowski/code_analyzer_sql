import glob
import re
import time

_file = open('log/%s.log' % str(time.time()), 'w')


def log(_line):
    _file.write(_line + "\n")


def get_select_sql(_html):
    p = re.compile('(.+select .+\n)', flags=re.I)
    return p.findall(_html)


def get_update_sql(_html):
    p = re.compile('(.+update .+\n)', flags=re.I)
    return p.findall(_html)


def get_where_sql(_html):
    p = re.compile('(.+where .+\n)', flags=re.I)
    return p.findall(_html)


def get_delete_sql(_html):
    p = re.compile('(.+delete .+\n)', flags=re.I)
    return p.findall(_html)


def get_order_by_sql(_html):
    p = re.compile('(.+order by .+\n)', flags=re.I)
    return p.findall(_html)


def read_file(file_full_path):
    with open(file_full_path, 'r') as myfile:
        data = myfile.read()
        return data


def analyze_file(file_full_path):
    content = read_file(file_full_path)

    select_sql = get_select_sql(content)
    update_sql = get_update_sql(content)
    where_sql = get_where_sql(content)
    delete_sql = get_delete_sql(content)
    order_sql = get_order_by_sql(content)

    if len(select_sql) or len(update_sql) or len(where_sql) or len(order_sql) or len(delete_sql):

        log("-------------------------------------")
        log("File path: " + file_full_path)

        for sql in select_sql:
            log("- SELECT - " + sql)
        for sql in update_sql:
            log(" - UPDATE - " + sql)
        for sql in where_sql:
            log(" - WHERE - " + sql)
        for sql in delete_sql:
            log(" - DELETE - " + sql)
        for sql in order_sql:
            log(" - ORDER - " + sql)


def init(_path, _file_extension):
    print("Start")
    files = glob.glob(_path + '/**/*' + _file_extension, recursive=True)

    log("Number of files: " + str(len(files)))

    for file in files:
        analyze_file(file)
    print("End")


init('/home/Workspace/java-project', ".java")
