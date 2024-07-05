import React, { useState, useEffect } from 'react';
import { API, Auth } from 'aws-amplify';

function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    const apiName = 'ecommerceAPI';
    const path = '/products';
    const response = await API.get(apiName, path);
    setProducts(response);
  };

  const addToCart = async (productId) => {
    const apiName = 'ecommerceAPI';
    const path = '/cart';
    const myInit = {
      body: { productId },
    };
    const response = await API.post(apiName, path, myInit);
    setCart(response);
  };

  const checkout = async () => {
    const apiName = 'ecommerceAPI';
    const path = '/checkout';
    const response = await API.post(apiName, path);
    alert(response.message);
  };

  return (
    <div className="App">
      <h1>Product Catalog</h1>
      <div className="products">
        {products.map((product) => (
          <div key={product.id}>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <button onClick={() => addToCart(product.id)}>Add to Cart</button>
          </div>
        ))}
      </div>
      <h1>Shopping Cart</h1>
      <div className="cart">
        {cart.map((item) => (
          <div key={item.productId}>
            <h2>{item.productName}</h2>
            <p>{item.quantity}</p>
          </div>
        ))}
      </div>
      <button onClick={checkout}>Checkout</button>
    </div>
  );
}

export default App;
