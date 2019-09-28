import json
import requests
import csv

#functiron return True is url is valid
def check_url(url="", redirects=True):
    result=False
    try:
        connect_url = requests.get(url, allow_redirects=redirects)
    except requests.RequestException:
        return False
    status = connect_url.status_code
    body_content = str(connect_url.content)
    if status in required_status_code and status not in except_status_code:
        result=True
        if any(i in body_content for i in required_strings) or not required_strings:
            result=True
            if any(j not in body_content for j in not_required_strings)or not not_required_strings:
                result=True
            else:
                result=False
        else:
            result=False
    else:
        result=False
    return result

#loop throught json
def get_all(myjson, key, invalied_urls):
    if type(myjson) == str:
        myjson = json.loads(myjson)
    if type(myjson) is dict:
        for jsonkey in list(myjson):
            if type(myjson[jsonkey]) in (list, dict):
                get_all(myjson[jsonkey], key, invalied_urls)
            elif jsonkey == key:
                is_url_valid = check_url(myjson["url"],redirects=False)
                if is_url_valid == False:
                    invalied_urls.append(myjson["url"])
    elif type(myjson) is list:
        for item in myjson:
            if type(item) in (list, dict):
                get_all(item, key, invalied_urls)
    return invalied_urls


def read_json_from_bookmarks(file_name):    
    with open(file_name, encoding="utf_8") as json_file:
        data = json.load(json_file)
    return data

def export_invalid_urls_to_csv(output,links_list):
    with open(output, 'w', encoding="utf_8") as outfile:
        for item in links_list:
            outfile.write("%s\n" %item)



if __name__ == '__main__':
    global required_status_code
    global except_status_code
    global required_strings
    global not_required_string

    required_status_code=(200,301)
    except_status_code=(400,500)
    required_strings=[]
    not_required_strings=[]

    invalied_urls=[]

    json_file_name = "bookmarks_testing"
    output_file="file_invalid_urls.txt"

    json_data_bookmarks = read_json_from_bookmarks(json_file_name)

    get_all(json_data_bookmarks, 'url', invalied_urls)

    export_invalid_urls_to_csv(output_file,invalied_urls)



