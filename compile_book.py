import os


def get_files_in_dir(directory):
    return sorted(os.listdir(directory))


header = '<!DOCTYPE html>\n<html class="no-js" lang="en">\n<html>\n<head>\n<meta charset="utf-8">\n<title>Kotlin</title>\n<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n</head>\n<body>\n'
footer = '\n</body>\n</html>'
result_html = header

read_directory = os.getcwd() + '/html-for-book/'
files_list = get_files_in_dir(read_directory)
count = 0
for html_page in files_list:
    a = ''
    with open(read_directory + html_page) as html_file:
        a = html_file.readlines()
        a = ''.join(a)
    article_str = '\n' + a[a.find('<article') : a.find('</article>') + len('</article>')] + '\n'
    result_html += article_str
    print html_page, 'added'
    count += 1
result_html += footer
print 'Articles added', count

with open(os.getcwd() + '/result.html', 'w') as res:
    res.write(result_html)
    print 'HTML finished'
