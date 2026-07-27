# How to Create a Collection in Postman (Step-by-Step)

Collections help you organize related API requests into one place. In
this example, we'll create a collection for **Cisco SD-WAN APIs**.

## Step 1: Open Postman

Launch the Postman desktop application.

## Step 2: Go to Collections

In the left sidebar, click **Collections**.

## Step 3: Create a New Collection

Click the **+** button next to **Collections**, or click **New** →
**Collection**.

## Step 4: Name the Collection

Enter a name for your collection.

**Example:**

``` text
Cisco SD-WAN APIs
```

## Step 5: Create the Collection

Click **Create**.

Your new collection will appear in the Collections list.

## Step 6: Add Your First Request

Hover over the **Cisco SD-WAN APIs** collection and click **Add
request**.

Name the request:

``` text
Get Devices
```

Click **Save to Cisco SD-WAN APIs**.

## Step 7: Configure the Request

Set the request method to:

``` text
GET
```

Enter the request URL:

``` text
https://<vmanage-ip>/dataservice/device
```

Replace `<vmanage-ip>` with the hostname or IP address of your Cisco
SD-WAN vManage server.

## Step 8: Save the Request

Click **Save**.

The request is now stored inside your **Cisco SD-WAN APIs** collection.

## Step 9: Add Another Request

Click the **...** next to the collection and select **Add request**.

Name it:

``` text
Get Device Status
```

Use:

**Method**

``` text
GET
```

**URL**

``` text
https://<vmanage-ip>/dataservice/device/monitor
```

Click **Save**.

## Step 10: Organize More Requests

Continue adding additional SD-WAN API requests to the collection, such
as:

-   Login
-   Get Devices
-   Get Device Status
-   Get Device Inventory
-   Get Control Connections
-   Get Interfaces
-   Get BFD Sessions
-   Get Device Templates
-   Get Device Template Attachments

As your collection grows, you can also organize requests into folders
for categories like **Devices**, **Monitoring**, **Templates**, and
**Policies**.

## That's It!

You have successfully created a Postman collection and added multiple
Cisco SD-WAN API requests. Keeping related requests in a collection
makes them easier to manage, test, and share with your team.
