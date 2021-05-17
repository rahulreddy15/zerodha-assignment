import axios from "axios";

export default class ProductService {
  getEquityData() {
    return axios
      .get("http://localhost:8000/api/dailyData")
      .then((res) => res.data);
  }
}
