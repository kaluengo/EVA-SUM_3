console.log()
const listaves= async() => {
    const response= await fetch("https://aves.ninjas.cl/api/birds");
    const aves= await response.json();
    
    let tablebody = ``;
    aves.forEach((user, api) => {
        tablebody += `<tr>
        <td class='centered'>${user.uid}</td>
        <td class='centered'>${user.name.spanish}</td>
        <td class='centered' ><img class='centered' src="${user.images.thumb}"></img></td>
        </tr>`;

    });
    // document.getElementById("tablebody_aves").innerHTML = tablebody
    tablebody_aves.innerHTML = tablebody;
        
        
    
    


};


window.addEventListener("load",function(){
    console.log("documento cargado")
    listaves();

});