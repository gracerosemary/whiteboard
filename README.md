# Back End Deployment  

PR Link: 

**Author**: G Choi   
**Version**: 1.0.0

## Overview
Create a DRF powered API and adjust project's permissions for authenticated access only. Add custom permissions to update/delete and add ability for user's to switch from API. Add JWT Authentication. Make sure data persists. Modify application to store db information in .env file. Deploy application on a host site of your choice. 

## Architecture
Django, Docker, Postgres, Poetry, Whitenoise, djangorestframework-simplejwt, HTTPie, Gunicorn, Django-Cors-header     

## API
Project - Whiteboard Interview Practice  
Choose your structure, method, action to practice for a whiteboard interview. Add the problem domain, upload your visual, Big O, algorithm, pseudo code, code, and verification.  

## Getting to deployed site:
Admin Site: https://wb-interview.herokuapp.com/admin/  
User credentials: (in submission notes)  
Click 'Whiteboards' to add a new whiteboard!    

Main Site: https://wb-interview.herokuapp.com/api/v1/wb/    
Expected behavior: ""Authentication credentials were not provided."    

Is the site connected properly?  
`$ curl -v https://wb-interview.herokuapp.com/admin/` should display:  
> `< HTTP/1.1 302 Found`

## Change Log
03-27-2021 6:53pm - Tried to deploy on AWS   
03-28-2021 9:00pm - Tried to deploy on AWS  
03-29-2021 8:45pm - Deployed successfully on Heroku  