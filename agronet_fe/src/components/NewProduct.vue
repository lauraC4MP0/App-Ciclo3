<template>
  <div class="main-component">
    <form v-on:submit.prevent="processNewProduct">
      <h2>Agregar nuevo producto</h2>
      <input
        type="text"
        v-model="product.name_product"
        placeholder="Nombre del producto"
        required
      />
      <br />
      <textarea
        name="description"
        maxlength="300"
        placeholder="Descripción del producto (máximo 300 carácteres)"
        v-model="product.description_product"
      ></textarea>
      <label>Precio unitario (pesos colombianos):</label>
      <input
        type="number"
        v-model="product.price_product"
        min="1000"
        required
        placeholder="1000.00"
      />
      <br />
      <label>Unidad de venta:</label>
      <br />
      <select v-model="product.sales_unit_product">
        <option value="Kilogramo">Kilogramo</option>
        <option value="Libra">Libra</option>
        <option value="Gramo">Gramo</option>
        <option value="Litro">Litro</option>
        <option value="Mililitro">Mililitro</option>
      </select>
      <select class="id" v-model="product.username_fk">
        <option disabled selected>Selecciona tu cédula</option>
        <option v-for="user in users" :key="user" :value="user.id">
          {{ user.id }}
        </option>
      </select>
      <div class="amount">
        <h2>Cantidad</h2>
        <label>(en unidades de venta) que tienes disponibles para venta.</label>
        <center>
          <input type="number" placeholder="1" min="1" required v-model="product.amount_product"/>
        </center>
        <br />
        <label
          >Si vendes por libras, debes poner cuántas libras tienes
          disponibles.</label
        >
      </div>
      <label>Adjuntar imagen (opcional):</label>
      <br />
      <br />
      <input type="file" name="image" accept="image/png, image/jpg" />
      <br />
      <button type="submit">Crear producto</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "NewProduct",
  data: function () {
    return {
      product: {
    name_product: "",
    description_product: "",
    price_product: null,
    sales_unit_product: "",
    username_fk: null,
    amount_product: null,
    image_product: null
},
      users: [],
    };
  },
  created: async function () {
    this.getUsers();
  },
  methods: {
    processNewProduct: function () {
      console.log(this.product);
      axios
        .post(
          "https://ciclo3grupo2agroclicbd.herokuapp.com/product/",
          this.product,
          { headers: {} }
        )
        .then((result) => {
          let dataNewProduct = {
            name_product: this.product.name_product,
          };
          this.$emit("completedNewProduct", dataNewProduct);
        })
        .catch((error) => {
          console.log(error);
          alert("Ha ocurrido un error en el registro");
        });
    },
    getUsers: function () {
      axios
        .get("https://ciclo3grupo2agroclicbd.herokuapp.com/user/")
        .then((result) => {
          this.users = result.data;
        })
        .catch((error) => {
          console.log(error);
          alert("No hay usuarios disponibles");
        });
    },
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;

  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
form {
  width: 500px;
  padding: 16px;
  border-radius: 10px;
  margin: auto;
  background-color: mediumaquamarine;
  margin-top: 20px;
}
textarea {
  width: 400px;
  border-radius: 10px;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-size: 18px;
}
.amount {
  width: 450px;
  padding: 16px;
  padding-top: 1px;
  background-color: white;
  border-radius: 10px;
  margin-top: 0;
  align-items: center;
  align-content: center;
  border-top: 0;
}
.main-component label {
  font-size: 18px;
}
.amount h2 {
  border-top: 0;
}
.amount select {
  align-items: center;
  align-content: center;
  align-self: center;
}
form h3 {
  height: 0;
  padding: 0%;
}
form input[type="text"],
form input[type="email"],
form input[type="tel"],
form input[type="password"],
select,
form input[type="number"] {
  width: 450px;
  padding: 3px 10px;
  border: 1px solid white;
  border-radius: 3px;
  background-color: white;
  margin: 8px 0;
  display: inline-block;
  font-size: 18px;
}
form input[type="radio"] {
  font-style: italic;
  font-size: 18px;
  padding: 0;
}
form .amount input[type="number"] {
  background-color: white;
  width: 40px;
  height: 40px;
  border: 1px solid black;
  border-radius: 3px;
  align-content: center;
  align-items: center;
}
form button {
  width: 100%;
  padding: 8px 16px;
  margin-top: 28px;
  border-radius: 5px;
  border: 1px solid #000;
  display: block;
  color: white;
  background-color: #000;
}
form button:hover {
  cursor: pointer;
}

textarea {
  width: 100%;
  height: 100px;
  border: 1px solid white;
  margin: 8px 0;
  resize: none;
  display: block;
}
</style>
