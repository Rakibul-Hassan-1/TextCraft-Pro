import { Card, CardContent } from "../ui/card";
import { Button } from "../ui/button";

import { ShoppingCart } from "lucide-react";
import React, { useState } from "react";

const products = [
  { id: 1, name: "Product A", price: 29.99 },
  { id: 2, name: "Product B", price: 39.99 },
  { id: 3, name: "Product C", price: 49.99 },
];

export default function ProductSellingApp() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-center">Product Store</h1>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {products.map((product) => (
          <Card key={product.id} className="p-4 shadow-lg rounded-2xl border">
            <CardContent className="flex flex-col items-center">
              <h2 className="text-lg font-semibold mb-2">{product.name}</h2>
              <p className="text-gray-600 text-sm">
                ${product.price.toFixed(2)}
              </p>
              <Button
                className="mt-3 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
                onClick={() => addToCart(product)}
              >
                Add to Cart
              </Button>
            </CardContent>
          </Card>
        ))}
      </div>
      <div className="mt-8 p-6 border rounded-lg shadow-md bg-gray-100">
        <h2 className="text-xl font-bold flex items-center justify-center mb-4">
          <ShoppingCart className="mr-2" /> Cart ({cart.length})
        </h2>
        {cart.length > 0 ? (
          <ul className="mt-2 space-y-2">
            {cart.map((item, index) => (
              <li
                key={index}
                className="text-gray-700 bg-white p-2 rounded-md shadow-sm border"
              >
                {item.name} - ${item.price.toFixed(2)}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-500 mt-2 text-center">Your cart is empty.</p>
        )}
      </div>
    </div>
  );
}
