import axios from "axios";

export default class ProductService {
  getEquityData() {
    return axios.get("/api/data");
  }
}
