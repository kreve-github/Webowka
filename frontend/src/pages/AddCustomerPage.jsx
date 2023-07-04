import { MainNav } from "@/components/MainNav";
import { navigationLinks } from "../config/navigationLinks";
import { UserNav } from "./CustomersPage/components/UserNav";
import { useState } from "react";

const CreateCustomer = () => {
  const [customerData, setCustomerData] = useState({
    name: "",
    surname: "",
    email: "",
    phone_number: ""
  })

  const onSubmitHandler = () => {
    fetch("http://localhost:8000/customers/add-customer", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(customerData)
    })
  }

  const onChangeHandler = (e) => {
    const { name, value } = e.target;
    setCustomerData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };
  
  return (
    <form onSubmit={onSubmitHandler}>
      <label>
        Name: <input type="text" name="name" value={customerData.name} onChange={onChangeHandler}></input>
      </label>
      <br /><br />
      <label>
        Surname: <input type="text" name="surname" value={customerData.surname} onChange={onChangeHandler}></input>
      </label>
      <br /><br />
      <label>
        Email: <input type="text" name="email" value={customerData.email} onChange={onChangeHandler}></input>
      </label>
      <br /><br />
      <label>
        Phone Number: <input type="text" name="phone_number" value={customerData.phone_number} onChange={onChangeHandler}></input>
      </label>
      <br /><br />
      <button type="submit">Create Customer</button>
    </form>
  )
}


export const AddCustomerPage = () => {
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
          <h2 className="text-3xl font-bold tracking-tight">Add customer</h2>
          
        </div>
        <div className="hidden h-full flex-1 flex-col space-y-8 md:flex"></div>
        <CreateCustomer />
      </div>
    </div>
  );
};
