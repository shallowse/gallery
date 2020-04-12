import os
import sys
from datetime import datetime

# s == 'kuva-10.jpg'
def _comparison_key(s):
    s = s.split('.')[0]
    s = s.split('-')[1]
    return int(s)

def main():
    image_dir = sys.argv[1]

    with open('index.tmpl', 'r') as f:
        data = f.read()

    # replace {{headerStr}}
    today = datetime.now().strftime("%d.%m.%Y")
    data = data.replace('{{headerStr}}', 'Kuvia - Generoitu: ' + today)

    # replace {{rows}}
    a = os.listdir(image_dir)
    a.sort(key=_comparison_key) 

    format_string = '<div class="col-12 col-lg-3 col-md-6"><a href="img/{{X}}"><img src="thumb-img/{{X}}" class="img-fluid"></a></div>\n\t\t'

    rows = ''
    for v in a:
       rows += format_string.replace('{{X}}', v) 
    data = data.replace('{{rows}}', rows) 

    # write the index.html
    with open('index.html', 'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
