## VCFAPI



### First:
1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r ./vcfapiproject/requirements.txt

### Install reusable app:
cd django-vcfapi && python3 run.py && cd ..

### Database:
1. cd vcfapiproject
2. python3 manage.py makemigrations
3. python3 manage.py migrate
4. python3 manage.py createsuperuser

### Execute:
1. cd vcfapiproject (if not)
2. python3 manage.py runserver

### Go to:
http://127.0.0.1:8000/admin/

- Insert token:
![Screenshot](create_token.png)

- Upload vcf file and open url to navigate:
![Screenshot](upload_vcf_and_open_url.png)

- Api format for browser:
![Screenshot](api_format.png)

- Searching item:
![Screenshot](search_item.png)

http://127.0.0.1:8000/

### Notes:
- (Use web interface and/or direct calls)
1. curl 'http://127.0.0.1:8000/custom-auth-token/' -H "Authorization:Token aa083c197a879f3968671bf237710bfd8dff10e0"
2. Authentication token implemented as param "auth_token" in CustomAuthTokenView view. It can also be used in web interface
3. BrowsableAPIRenderer (api format for browser):
http://127.0.0.1:8000/file/4/records/?format=api
4. JSONRenderer:
curl 'http://127.0.0.1:8000/file/4/records/'
5. JSONRenderer: 
curl 'http://127.0.0.1:8000/file/4/records/?limit=10&offset=30' -H "Accept: */*"
6. JSONRenderer:
curl 'http://127.0.0.1:8000/file/4/records/?limit=10&offset=30' -H "Accept: application/json"
7. XMLRenderer:
curl 'http://127.0.0.1:8000/file/4/records/?limit=10&offset=30' -H "Accept: application/xml"
8. Retrieve selected records:
curl 'http://127.0.0.1:8000/file/4/records/?limit=1000&id=rs75935175' -H "Accept: application/json"


### TODO:
1. Create custom pagination for large files
2. 
3. 
4. 
5. 
