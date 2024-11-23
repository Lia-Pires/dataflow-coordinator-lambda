# DataFlow Coordinator

## Overview

**DataFlow Coordinator** is a serverless solution designed to process and route dynamic payloads to the appropriate database tables using **AWS Lambda**. Triggered by events from **Amazon SQS**, the Lambda function processes incoming messages and determines which tables need to be updated based on the data within the payload. This architecture offers flexibility and scalability, allowing you to easily manage data updates without complex infrastructure management.

## Features

- **Event-Driven**: Processes data in real-time with AWS Lambda, triggered by messages from **Amazon SQS**.
- **Scalable**: Automatically scales based on the number of messages in the SQS queue, minimizing operational overhead.
- **Flexible**: Handles various types of data payloads and dynamically routes them to the correct tables.
- **Easy Integration**: Seamlessly integrates with other AWS services like **SNS**, **API Gateway**, and **RDS**.
- **Minimal Configuration**: Organizes payloads and updates tables with minimal manual intervention, reducing complexity.

## Architecture

- **AWS Lambda**: Processes payloads from the SQS queue and directs them to the appropriate database tables.
- **Amazon SQS**: The event source that triggers the Lambda function, delivering payloads in the form of messages.
- **Database**: Relational database (e.g., **AWS RDS**, **Aurora**) where the data is stored and updated. Tables include entities such as `Customers`, `Purchases`, `Products`, etc.

## Use Cases

### 1. **Customer Updates**
Automatically updates customer details, such as:
- **Personal Information**: Name, email, contact details.
- **Address Management**: Shipping and billing addresses.
- **Subscription/Preferences**: Subscription plans, marketing preferences.

**Payload Example**:

```json
{
    "customer_id": 123,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "shipping_address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postal_code": "12345"
    }
}
```


### 2. **Purchase Processing**
Handles the creation and updating of purchase transactions, including:

- **Order Details**: Items, quantities, prices.
- **Payment Information**: Total amounts, status (paid, pending).
- **Order Status Updates**: Shipping, delivery, and returns.

**Payload Example**:

```json
{
    "purchase_id": 456,
    "customer_id": 123,
    "items": [
        {
            "product_id": 789,
            "quantity": 2,
            "price": 99.99
        }
    ],
    "total_amount": 199.99,
    "status": "paid"
}
```






### 3. **Product Management**
Easily updates product catalogs with:

- **Stock Levels**: Quantity, availability.
- **Price Updates**: New price, discounts.
- **Product Attributes**: Description, categories, specifications.

### Payload Example:
```json
{
    "product_id": 789,
    "name": "Wireless Mouse",
    "price": 49.99,
    "stock_quantity": 150,
    "category": "Electronics"
}
```



### 4. **Subscription Service Management**
Manages updates related to subscription services, including:

- **Subscription Plans**: New subscriptions, upgrades, downgrades.
- **Billing Information**: Billing cycles, next payment date.
- **Status Updates**: Active, paused, or canceled subscriptions.

### Payload Example:

```json
{
    "subscription_id": 101,
    "customer_id": 123,
    "plan": "Premium",
    "status": "active",
    "next_billing_date": "2024-12-01"
} 
```

### 5. **User Activity Tracking**
Tracks user interactions and activity, such as:

- **Login Events**: Timestamp, IP address, device used.
- **Behavioral Analytics**: Product views, cart additions, clickstream data.

### Payload Example:

```json
{
    "user_id": 123,
    "activity_type": "login",
    "timestamp": "2024-11-23T10:15:00Z",
    "device": "mobile",
    "ip_address": "192.168.1.1"
}
```


### 6. **Inventory and Stock Management**
Monitors and updates inventory levels based on:

- **Stock Restocks**: New inventory shipments.
- **Stock Movements**: Item transfers between warehouses, returns.
- **Low Stock Alerts**: Trigger notifications when stock falls below a threshold.

### Payload Example:
```json
{
    "product_id": 789,
    "restocked_quantity": 100,
    "warehouse_id": 2,
    "stock_threshold": 20
} 
```


## Installation

### Prerequisites
- **AWS Account**: Ensure you have an AWS account with Lambda, SQS, and database access.
- **AWS CLI**: Installed and configured for deployment.
- **Node.js/Python**: Depending on your Lambda function language (adjust accordingly).

### Steps to Deploy

1. **Clone this repository**:
    bash
    git clone https://github.com/lia-pires/dataflow-coordinator-lambda.git
    cd dataflow-coordinator-lambda
    

2. **Configure AWS credentials**: Make sure your AWS credentials are set up using the AWS CLI or environment variables.

3. **Create an SQS Queue**:  
   Create an SQS queue that will trigger the Lambda function when new messages arrive.

   Example (using AWS CLI):
    bash
    aws sqs create-queue --queue-name dataflow-queue
    

4. **Deploy Lambda**:
   Deploy the Lambda function using AWS SAM, Serverless Framework, or CloudFormation.
   Configure the Lambda function to be triggered by the SQS queue you created.

5. **Test the Lambda function**:
   Send test messages to the SQS queue and confirm that the Lambda function processes them and updates the correct database tables.

## Configuration

### Environment Variables
The following environment variables are required for Lambda to connect to the database and handle dynamic payloads:

- **DB_HOST**: Hostname of the database.
- **DB_USER**: Database username.
- **DB_PASSWORD**: Database password.
- **DB_NAME**: The database name.
- **TABLES**: Comma-separated list of tables to be updated.

### Payload Structure
Each type of payload will follow a structure based on the use case (see examples above). The Lambda function will inspect the payload to decide which database table to update.

### SQS Integration
- **Event Source**: The Lambda function is triggered by messages from SQS.
