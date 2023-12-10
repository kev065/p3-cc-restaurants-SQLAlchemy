
# To query the database, run the following commands to return for each particular instance: 

1. ### Return the customer instance:
    ```
    customer = session.query(Customer).filter_by(id=customer_id).first()
    ```
    e.g.
    ```
    customer = session.query(Customer).filter_by(id=1).first()
    print(customer.first_name, customer.last_name)
    # => Kevin Marks
    ```

2. ### Return the restaurant instance:
    ```
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).first()
    ```
    e.g.
    ```
    restaurant = session.query(Restaurant).filter_by(id=2).first()
    print(restaurant.name)
    # => Benson-Blevins
    ```

3. ### Return a collection of all reviews from the restaurant:
    ```
    restaurant_reviews = session.query(Review).filter_by(restaurant_id=restaurant_id).all()
    ```
    e.g. 
    ```
    restaurant_reviews = session.query(Review).filter_by(restaurant_id=1).all()
    for review in restaurant_reviews:
        print(review.full_review())
    # => Review for Williams and Sons by Tonya Miller: 1 stars.
         Review for Williams and Sons by Caleb Bruce: 5 stars.
         Review for Williams and Sons by Mark Johnson: 2 stars.
         Review for Williams and Sons by Tonya Miller: 4 stars.
    ```


4. ### Return a collection of all customers who reviewed the restaurant:
    ```
    restaurant_customers = session.query(Customer).join(Review).filter(Review.restaurant_id == restaurant_id).all()
    ```
    e.g. 
    ```
    restaurant_customers = session.query(Customer).join(Review).filter(Review.restaurant_id == 3).all()
    for customer in restaurant_customers:
        print(customer.full_name())
    # => Ashley Valentine
         Jasmine Lewis
    

5. ### Return a collection of all the reviews that the Customer has made:
    ```
    customer_reviews = session.query(Review).filter_by(customer_id=customer_id).all()
    ```
    e.g. 
    ```
    customer_reviews = session.query(Review).filter_by(customer_id=4).all()
    for review in customer_reviews:
        print(review.full_review())
    # => Review for Williams and Sons by Tonya Miller: 1 stars.
         Review for Kirby and Sons by Tonya Miller: 2 stars.
         Review for Benson-Blevins by Tonya Miller: 1 stars.
         Review for Williams and Sons by Tonya Miller: 4 stars.
    ```

6. ### Return a collection of all the restaurants that the Customer has reviewed:
    ```
    customer_restaurants = session.query(Restaurant).join(Review).filter(Review.customer_id == customer_id).all()
    ```
    e.g.
    ```
    customer_restaurants = session.query(Restaurant).join(Review).filter(Review.customer_id == 3).all()
    for restaurant in customer_restaurants:
        print(restaurant.name)
    # => Kirby and Sons
         Foley Group
         Kim-Jimenez
    ```
