import { MainNav } from "@/components/MainNav";

import { DataTable } from "./components/DataTable";
import { Columns } from "./components/Columns";
import { UserNav } from "./components/UserNav";
import { navigationLinks } from "../../config/navigationLinks";
import { useEffect, useState } from "react";



const getOrdersList = () => {
  const [orders, setOrders] = useState([])

  const fetchOrdersData = () => {
    fetch("http://localhost:8000/orders")
      .then(response => response.json())
      .then((data) => {
        const orderData = data.map((order) => ({
          customer_name: order.customer_name,
          order_id: order.id,
          product_list: order.products_names,
          sum: `${order.sum} $`
        }))
        setOrders(orderData)
      })
  } 
  useEffect(() => {fetchOrdersData()}, [orders])
  return orders  
}


export const OrdersPage = () => {
  const ordersList = getOrdersList()
  return (
    <div className="hidden flex-col md:flex">
      <div className="border-b">
        <div className="flex h-16 items-center px-4">
          <MainNav className="mx-6" links={navigationLinks} />
          <div className="ml-auto flex items-center space-x-4">
            <UserNav />
          </div>
        </div>
      </div>
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <h2 className="text-3xl font-bold tracking-tight">Orders</h2>
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex">
          <DataTable
            data={ordersList}
            columns={Columns}
          />
        </div>
      </div>
    </div>
  );
};
