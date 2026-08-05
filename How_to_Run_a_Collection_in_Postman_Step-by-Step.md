# How to Run a Collection in Postman (Step-by-Step)

## Step 1
Open your collection and click **Run**.

## Step 2
Select these requests:
- ✅ Login
- ✅ Get Devices

## Step 3
Use these settings:
- **Run type:** Functional
- **Run method:** Local
- **Iterations:** 1

## Step 4
Enable:
- ✅ Persist responses for a session
- ✅ Stop run if an error occurs
- ✅ Keep variable values
- ✅ Save cookies after collection run

## Step 5
Click **Start run**.

## Step 6
Verify:
- ✅ Login → Status **200**
- ✅ Get Devices → Status **200**

> **Note:** Postman runs requests in the order they appear in the collection. The **Login** request runs first, allowing **Get Devices** to automatically use the **JSESSIONID** cookie.
