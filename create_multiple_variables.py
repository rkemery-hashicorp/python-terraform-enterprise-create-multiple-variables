import pyterprise

# Example dictionary
variables_dict = {
        "foo01": "bar01", 
        "foo02": "bar02",
        "foo03": "bar03"
        }

# TFE API Token
tfe_token = ''

# Client request
client = pyterprise.Client()

# Supply your token as a parameter and the url for the terraform enterprise server.
# If you are not self hosting, use the one provided by hashicorp.
client.init(token=tfe_token, url='https://terraform-enterprise-url')

# Set the organization
org = client.set_organization(id='exampletfeorg')

# Get a single workspace client object,
# you can also list or search all workspace objects using the corresponding methods.
workspace = org.get_workspace('workspace-name')

# Create a variable in a workspace - example for single
# workspace.create_variable(key='foo', value='bar', sensitive=False, category='terraform')

# Print items in variables dictionary
for x, y in variables_dict.items():
  print(x, y) 

# Iterate through dictionary and create variables based on key / value pairs
# Category can be env for environment variables
for x, y in variables_dict.items():
    workspace.create_variable(key=x, value=y, sensitive=False, category='terraform')
