# How to Create and Use Environments in Postman (Step-by-Step)

## Step 1: Open Your Workspace
Open Postman and switch to the workspace where you want to create the environment.

## Step 2: Open the Environments Page
In the left sidebar, click **Environments**.

## Step 3: Create a New Environment
Click **+** or **Create Environment**.

## Step 4: Enter an Environment Name
Give your environment a descriptive name, such as:
- Development
- Testing
- Production

## Step 5: Add Variables
Create the variables you need.

| Variable | Initial Value | Current Value |
|----------|---------------|---------------|
| `base_url` | `https://jsonplaceholder.typicode.com` | `https://jsonplaceholder.typicode.com` |

You can add more variables later, such as API keys or tokens.

## Step 6: Save the Environment
Click **Save**.

## Step 7: Select the Environment
Use the environment dropdown in the top-right corner and choose the environment you just created.

## Step 8: Use Environment Variables
Reference variables in your requests using double curly braces:

```
{{base_url}}/posts
```

Postman replaces `{{base_url}}` with the value from the selected environment.

## What You Learned

- Create a new environment
- Add environment variables
- Select an environment
- Use variables in API requests
