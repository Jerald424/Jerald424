import React, { useState } from "react";
import data from "../MOCK_DATA (1).json";

export default function SearchData() {
  const [search, setSearch] = useState();
  console.log(search);
  return (
    <div style={{ textAlign: "center", marginTop: "40px" }}>
      <input type="text" onChange={(e) => setSearch(e.target.value)} />
      {data
        .filter((user) => user.first_name.toLowerCase().includes(search) )
        .map((res) => {
          return (
            <>
              <p>{res.first_name}</p>
            </>
          );
        })}
    </div>
  );
}
