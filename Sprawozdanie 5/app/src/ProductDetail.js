import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import './App.css';

function BackButton(){
    return (
        <Link to='/shop/' className="goBackButtonContainer">
            <div className='goBackButton'>
                &lt;Powrót
            </div>
        </Link>
    )
}

function ProductDetail({ match }) {

    useEffect( () => {
        fetchProduct();
    }, []);

    const [product, setProduct] = useState({});

    const fetchProduct = async () => {
        const fetchProduct = await fetch(`http://127.0.0.1:8000/products/${match.params.id}/`);
        const product = await fetchProduct.json();
        setProduct(product);

    }

    return (
    <div className="productContainer">
        <BackButton />
        <h1 className="productName">{product.name}</h1>
        <div className="flexBreak"></div>
        <div className="productInfo">
            <h3 className="productPrice">Cena: {product.price}zł</h3>
            <h3>Pozostało {product.in_stock} produktów!</h3>
        </div>
        <div className="flexBreak"></div>
        <h3 className="descriptionText">Opis:</h3>
        <div className="flexBreak"></div>
        <h2 className="productDescription">{product.description}</h2>
    </div>
  );
}

export default ProductDetail;