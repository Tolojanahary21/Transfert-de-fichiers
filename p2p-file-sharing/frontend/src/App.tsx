import { useEffect } from "react";
import api from "./api/axios";

function App() {

  useEffect(() => {

    api.get("/")
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.log(error);
      });

  }, []);


  return (
    <>
      <h1>P2P File Sharing</h1>
    </>
  )
}

export default App;