# 1. Calculate Average Rating and Number of Reviews by Product Categories
# Hint: Group the data by product categories. Use aggregation functions like mean() for the average rating and count() for the number of reviews.

df1 = pd.merge(df_items[['order_id','product_id']],df_products[['product_category_name','product_id']],how='left',on='product_id')
df2 = pd.merge(df_items[['order_id']], df_reviews[['review_id','review_score','order_id']], how = 'left', on = 'order_id')
df = pd.merge(df1,df2,how='left',on='order_id')
df.groupby('product_category_name').agg(Average_Rating = ('review_score','mean'), Number_of_Reviews = ('review_id','count'))

# 2. Number of Orders, and Sales by Product Categories
# Hint: Group by product categories and calculate the total number of orders, and total sales (payment_value).

df1 = pd.merge(df_products[['product_id','product_category_name']],df_items[['order_id','product_id']],how = 'left', on = 'product_id')
df1 = pd.merge(df1[['order_id','product_category_name']],df_payments[['order_id','payment_value']],how='left',on='order_id')
df1.groupby('product_category_name').agg(Number_of_Orders = ('order_id','count'), Number_of_Sales = ('payment_value','sum'))

# 3. Which States Have the Highest Number of Customers?
# Hint: Group the data by the state and count the number of distinct customers. You can use groupby() and nunique() to count unique customers by state.

df = df_customers.groupby('customer_state')['customer_id'].nunique() # đếm số lượng khách hàng khác nhau (distinct customers)
df.sort_values(ascending = False).reset_index()

# 4. Top 5 Customers Generating the Most Revenue
# Hint: Group by customer and sum the total revenue (payment_value). Sort the results in descending order and select the top 5.

df = pd.merge(df_orders[['order_id','customer_id']],df_payments[['order_id','payment_value']],how='left',on='order_id')
df = df.groupby('customer_id').agg(Total_revenue = ('payment_value','sum')).reset_index()
df.sort_values('Total_revenue',ascending = False).head(5)

# 5. Number of Orders for Each Category ("Morning", "Afternoon", "Evening", "Night")
# Categorize purchase time based on the order_purchase_timestamp hour:
# Morning for hours between 5 AM and 12 PM.
# Afternoon for hours between 12 PM and 5 PM.
# Evening for hours between 5 PM and 9 PM.
# Night for hours between 9 PM and 5 AM.
# Hint: Categorize the purchase time based on the order_purchase_timestamp hour. Use the .dt accessor to extract the hour, then categorize the hour into "Morning", "Afternoon", "Evening", or "Night".

df_orders['order_purchase_timestamp'] = pd.to_datetime(df_orders['order_purchase_timestamp']) 
df_orders['time_to_order']=df_orders['order_purchase_timestamp'].dt.hour
def time_to_order(x):
  if 5 <= x < 12:
     return('Morning')
  if 13 <= x < 17:
     return('Afternoon')
  if 17 <= x < 21:
     return('Evening')
  else:
     return('Night')
df_orders['time_to_order_category'] = df_orders['time_to_order'].apply(time_to_order)
# df_orders['time_to_order_category'] = df_orders['time_to_order'].apply(lambda x: 'Morning' if x>5 else('Afternoon' if x<17 else('Evening' if x < 21 else 'Night')))
df_orders.groupby('time_to_order_category').agg(number_of_oders = ('order_id','count')).reset_index()

# 6. Total Number of Orders, and Sales by Day of the Week
# Hint: Extract the day of the week from the order_purchase_timestamp and group by this day. You can use .dt.day_name() or .dt.weekday to get the day name.

df = pd.merge(df_payments[['order_id','payment_value']],df_orders[['order_id','order_purchase_timestamp']],how='left',on='order_id')
df['order_purchase_timestamp'] = df['order_purchase_timestamp'].dt.day_name()
# cách lấy ngày trong tuần theo số .dt.dayofweek, .dt.weekday
# cách lấy ngày trong tuần theo chữ .dt.day_name()
df.groupby('order_purchase_timestamp').agg(number_of_order = ('order_id','count'), total_sales = ('payment_value','sum')).reset_index()

# 7. Average Rating Based on the Difference Between the Estimated and Actual Delivery Dates
# Hint:
# Calculate the difference between the order_estimated_delivery_date and the order_delivered_customer_date in terms of days.
# Categorize the delivery status based on the following conditions:
# If the difference is more than 10 days, categorize it as "late over 10 days".
# If the difference is between 5 and 10 days, categorize it as "late from 5 days to 10 days".
# If the difference is less than 5 days, categorize it as "late under 5 days".
# If the difference is 0 or greater, categorize it as "on time delivery".
# Calculate the average rating based on the est_to_deliver_detail column.
# Notes:
# Make sure to check the datatype of the columns you are working with, especially dates. You may need to use pd.to_datetime() for conversion.
# For categorizing timestamps or dates, use .dt to extract the components such as day, hour, or month.
# When performing aggregations, use groupby() to group by the relevant column and apply aggregation functions such as mean(), sum(), count(), or nunique().

lst = ['order_delivered_customer_date','order_estimated_delivery_date']
for i in lst:
  df_orders[i]=df_orders[i].str.split().str[0]
for i in lst:
  df_orders[i]=pd.to_datetime(df_orders[i])
df_orders['diff'] = df_orders['order_estimated_delivery_date'] - df_orders['order_delivered_customer_date']
df_orders['diff'].dt.days
def delivery_status_category(x):
  if x < pd.Timedelta(-10, unit = 'days'):
    return 'late over 10 days'
  if pd.Timedelta(-10, unit = 'days')<= x < pd.Timedelta(-5, unit = 'days'):
    return 'late from 5 days to 10 days'
  if pd.Timedelta(0, unit = 'days') <= x:
    return 'on time delivery' 
  if pd.Timedelta(-5, unit = 'days') <= x < pd.Timedelta(0, unit = 'days'):
    return 'late under 5 days'
df_orders['delivery_status_category']=df_orders['diff'].apply(delivery_status_category)
df = pd.merge(df_reviews[['order_id','review_score']],df_orders[['order_id','delivery_status_category']])
df.groupby('delivery_status_category').agg(average_rating = ('review_score','mean')).reset_index()
