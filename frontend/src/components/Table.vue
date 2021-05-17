<template>
  <div>
    <div>
      <h1>Equity Data Published By The BSE</h1>
      <h5>Last updated date: {{ date }}</h5>
      <DataTable
        :value="products"
        responsiveLayout="scroll"
        :paginator="true"
        removableSort
        :rows="10"
        paginatorTemplate="CurrentPageReport FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown"
        :rowsPerPageOptions="[10, 20, 50]"
        currentPageReportTemplate="Showing {first} to {last} of {totalRecords}"
      >
        <Column field="SC_CODE" header="Code" sortable="true"></Column>
        <Column field="SC_NAME" header="Name" sortable="true"></Column>
        <Column field="SC_GROUP" header="Group" sortable="true"></Column>
        <Column field="SC_TYPE" header="Type" sortable="true"></Column>
        <Column field="OPEN" header="Open" sortable="true"></Column>
        <Column field="HIGH" header="High" sortable="true"></Column>
        <Column field="LOW" header="Low" sortable="true"></Column>
        <Column field="CLOSE" header="Close" sortable="true"></Column>
        <Column field="LAST" header="Last" sortable="true"></Column>
        <Column
          field="NO_TRADES"
          header="Number Of Trades"
          sortable="true"
        ></Column>
      </DataTable>
    </div>
    <!-- <pre>
        <code>
            {{stringify(products)}}
        </code>
    </pre> -->
  </div>
</template>

<script>
// import ProductService from "./ProductService";
import axios from "axios";
export default {
  name: "Table",
  data() {
    return {
      products: null,
      date: null,
      count: null,
    };
  },
  productService: null,
  created() {},
  mounted() {
    axios.get("/api/dailyData").then((res) => {
      console.log(res.data);
      this.products = res.data.data;
      this.date = res.data.date;
      this.count = res.data.count;
    });
  },
  methods: {
    stringify(value) {
      return JSON.stringify(value, null, 2);
    },
  },
};
</script>
