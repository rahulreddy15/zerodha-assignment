<template>
  <div>
    <div>
      <h1>Equity Data Published By The BSE</h1>
      <h5>Last updated date: {{ date }}</h5>
      <DataTable
        :value="products"
        responsiveLayout="scroll"
        :paginator="true"
        ref="dt"
        removableSort
        :filters="filters"
        :loading="loading"
        :rows="10"
        paginatorTemplate="CurrentPageReport FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink RowsPerPageDropdown"
        :rowsPerPageOptions="[10, 20, 50]"
        currentPageReportTemplate="Showing {first} to {last} of {totalRecords}"
      >
        <template #header>
          <div style="text-align: left">
            <Button
              icon="pi pi-external-link"
              label="Export To CSV"
              @click="exportCSV($event)"
            />
          </div>
          <div class="text-align: right">
            <Button
              type="button"
              icon="pi pi-filter-slash"
              label="Clear"
              class="p-button-outlined"
              @click="clearFilter()"
            />
            <span class="p-input-icon-left">
              <i class="pi pi-search" />
              <InputText
                v-model="filters['global'].value"
                placeholder="Keyword Search"
              />
            </span>
          </div>
        </template>
        <template #loading>
          Loading customers data. Please wait.
        </template>
        <template #empty>
          No data found.
        </template>
        <Column field="SC_CODE" header="Code" sortable="true"></Column>
        <Column field="SC_NAME" header="Name" sortable="true"></Column>
        <Column field="OPEN" header="Open" sortable="true"></Column>
        <Column field="HIGH" header="High" sortable="true"></Column>
        <Column field="LOW" header="Low" sortable="true"></Column>
        <Column field="CLOSE" header="Close" sortable="true"></Column>
        <Column field="LAST" header="Last" sortable="true"></Column>
        <Column field="NO_TRADES" header="Trades" sortable="true"></Column>
        <Column field="NO_OF_SHRS" header="Shares" sortable="true"></Column>
        <Column field="NET_TURNOV" header="Turnover" sortable="true"></Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import { FilterMatchMode } from "primevue/api";
import axios from "axios";
export default {
  name: "Table",
  data() {
    return {
      products: null,
      date: null,
      count: null,
      filters: {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      },
      loading: true,
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
    this.loading = false;
  },
  methods: {
    stringify(value) {
      return JSON.stringify(value, null, 2);
    },
    exportCSV() {
      this.$refs.dt.exportCSV();
    },
    clearFilter() {
      this.initFilters();
    },
    initFilters() {
      this.filters = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
      };
    },
  },
};
</script>
