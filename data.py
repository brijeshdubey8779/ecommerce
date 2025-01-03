from index import db, Products, app

# List of product data to insert
product_data = [
    {
        "name": "Nike Air MX Super 2500 - Red",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 449,
        "original_price": 699,
        "discount": 39,
        "rating": 5.0,
        "reviews": 120
    },
    {
        "name": "Adidas UltraBoost 2025 - Black",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 199,
        "original_price": 250,
        "discount": 20,
        "rating": 4.8,
        "reviews": 150
    },
    {
        "name": "Apple AirPods Pro (2nd Gen)",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 249,
        "original_price": 299,
        "discount": 17,
        "rating": 4.7,
        "reviews": 230
    },
    {
        "name": "Sony WH-1000XM5 Wireless Headphones",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 379,
        "original_price": 449,
        "discount": 15,
        "rating": 4.9,
        "reviews": 180
    },
    {
        "name": "GoPro HERO12 Black",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 499,
        "original_price": 599,
        "discount": 17,
        "rating": 5.0,
        "reviews": 250
    },
    {
        "name": "Nike Air Force 1 '07 - White",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 109,
        "original_price": 130,
        "discount": 16,
        "rating": 4.8,
        "reviews": 90
    },
    {
        "name": "Canon EOS Rebel T8i DSLR Camera",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 899,
        "original_price": 999,
        "discount": 10,
        "rating": 4.9,
        "reviews": 300
    },
    {
        "name": "Samsung Galaxy Watch 5 Pro",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 449,
        "original_price": 499,
        "discount": 10,
        "rating": 4.6,
        "reviews": 120
    },
    {
        "name": "LG UltraGear 27GN950-B Gaming Monitor",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 649,
        "original_price": 799,
        "discount": 19,
        "rating": 4.8,
        "reviews": 200
    },
    {
        "name": "Bose SoundLink Revolve+ Bluetooth Speaker",
        "image_url": "https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c25lYWtlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60",
        "price": 299,
        "original_price": 349,
        "discount": 14,
        "rating": 4.7,
        "reviews": 180
    }
    ]

# Loop through the product data and create Product objects
for product in product_data:
    new_product = Products(
        name=product['name'],
        image_url=product['image_url'],
        price=product['price'],
        original_price=product['original_price'],
        discount=product['discount'],
        rating=product['rating'],
        reviews=product['reviews']
    )
    
    # Add the product to the session
    with app.app_context():
        db.session.add(new_product)
        db.session.commit()
        print("session")

    
    
# Query all products in the Product table
with app.app_context():
    products = Products.query.all()
    if products:
        print(products)

# Display the products
with app.app_context():
    for product in products:
        print(f"Product: {product.name}, Price: ${product.price}, Discount: {product.discount}%")
        print('data')

print("All products have been added successfully!")
