# p3-cc-restaurants-SQLAlchemy

### To query the database, run the following commands to return for each particular instance: 

1. Return the customer instance:
    ```
    customer = session.query(Customer).filter_by(id=customer_id).first()
    ```
    e.g.
    ```
    customer = session.query(Customer).filter_by(id=1).first()
    print(customer.first_name, customer.last_name)
    # => Kevin Marks

2. Return the restaurant instance:
    ```
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    ```

3. Return a collection of all reviews from the restaurant:
    ```
    restaurant_reviews = session.query(Review).filter_by(restaurant_id=restaurant_id).all()
    ```

4. Return a collection of all customers who reviewed the restaurant:
    ```
    restaurant_customers = session.query(Customer).join(Review).filter(Review.restaurant_id == restaurant_id).all()
    ```

5. Return a collection of all the reviews that the Customer has left:
    ```
    customer_reviews = session.query(Review).filter_by(customer_id=customer_id).all()
    ```

6. Return a collection of all the restaurants that the Customer has reviewed:
    ```
    customer_restaurants = session.query(Restaurant).join(Review).filter(Review.customer_id == customer_id).all()
    ```
