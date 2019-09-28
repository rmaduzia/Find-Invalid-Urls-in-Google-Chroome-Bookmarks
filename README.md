# Find-Invalid-Urls-in-Google-Chroome-Bookmarks

The script is designed to check whether the url pages contained in the tabs are working.

We can set parameters such as:

-Expected and unexpected server response code

-Expected and unexpected content on the page based on the String parameter

In variable "json_file_name" we define input json bookmarks from GoogleChrome

These variables are used to definie required parametrs:

    required_status_code=() number with comma separator

    except_status_code=() number with comma separator

    required_strings=[] string with comma seperator

    not_required_strings=[] string with comma seperator



