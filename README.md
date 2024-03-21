# Whispers of Wisdom: Inspiring Quotes for the Soul
![image](https://github.com/AbdelwadoudMakh55/Beautiful_Quotes/assets/133237331/187a1d21-ba5e-4092-b77e-9c4455f67693)
## Description:
Beautiful Quotes is a simple web application designed to provide users with random quotes along with images of the individuals who said them. This project utilizes Azure Functions for the backend API to fetch random quotes and associated images. The frontend is built using HTML, CSS, and JavaScript to create an engaging user experience.

## Features:
Random quote generation  
Display of quotes with corresponding images  
Simple and intuitive user interface  

## Architecture:
![Beautiful_Quotes_Architecture_v2](https://github.com/AbdelwadoudMakh55/Beautiful_Quotes/assets/133237331/adb6dec0-8fe6-4904-bccb-62714161a484)


## Technologies Used:
### Backend:

Azure Functions
### Frontend:

HTML  
CSS  
JavaScript 

## Usage:

`git clone https://github.com/AbdelwadoudMakh55/Beautiful_Quotes` 
#### To Install the Azure Functions Core Tools: [AzureFunctionsCoreTools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python#install-the-azure-functions-core-tools)
#### Navigate to the Quotes_API directory and run:
`pip install -r requirement.txt` to install the necessary requirements
#### Navigate to the local.settings.json file and add your container connection string:
`"AzureWebJobsStorage": "<connection_string>"`
#### Start the function locally:
`func start`
> [!NOTE]
> In order for your azure function to return a response you need to have a blob storage running

1. First Create a Microsoft Azure account.  
2. See here how to create your Blob Storage: https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-portal  

## Contributors
Abdelwadoud Makhlok ([@AbdelwadoudMakh55](https://github.com/AbdelwadoudMakh55))

## License
This project is available for anyone to use.
