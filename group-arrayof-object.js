import react from "react";

export default grouping(){
const details = [
  {name:"jerald", class:"10th", bloodgroup:"a+"},
  {name:"saba", class:"12th", bloodgroup:"b+"},
  {name:"kittu", class:"12th", bloodgroup:"a+"},
  {name:"thambi", class:"10th", bloodgroup:"o+"},
  {name:"peter", class:"11th", bloodgroup:"a+"},
  {name:"kannan", class:"10th", bloodgroup:"o+"},

];
  const result = details.reduce((acc, curr)=>{
      acc[curr.class] = [...(acc[curr.class] || []), curr];

  
  },{})
  console.log(result)
return (

)
}
