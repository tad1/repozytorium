import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import './App.css';

function Shop() {

    useEffect( () => {
        fetchProducts();
    }, []);

    const [products, setProducts] = useState([]);

    const fetchProducts = async () => {
        const data = await fetch("http://127.0.0.1:8000/products/")
        const products = await data.json();
        setProducts(products);
    }

    return (
    <div>
      <h1 className="productListName">Nasze Produkty:</h1>
      <ul className="productList">
      {products.map( product => ( 
        <li key={product.id}>
              <Link to={`/shop/${product.id}`}  className="productItem">
                {product.name}
              </Link>
              </li>
      ))}
      </ul>
    </div>
  );
}

export default Shop;