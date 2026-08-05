# How to Run Multiple API Requests in Postman (Step-by-Step)

## Step 1
Open your collection and click **Run**.

## Step 2
Select the requests to run:
- ✅ Login
- ✅ Get Devices

## Step 3
Configure the run:
- **Run type:** Functional
- **Run method:** Local
- **Iterations:** 1

## Step 4
Enable these settings:
- ✅ Persist responses for a session
- ✅ Stop run if an error occurs
- ✅ Keep variable values
- ✅ Save cookies after collection run

## Step 5
Click **Start run**.

## Step 6
Verify the results:
- ✅ Login → Status **200**
- ✅ Get Devices → Status **200**

> **Note:** Postman runs requests sequentially, following the order they appear in the collection. In this example, the **Login** request runs first, allowing **Get Devices** to automatically use the **JSESSIONID** cookie.
