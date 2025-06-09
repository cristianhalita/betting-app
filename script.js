function calculeaza() {
  const cote = [
    parseFloat(document.getElementById("cota1").value),
    parseFloat(document.getElementById("cota2").value),
    parseFloat(document.getElementById("cota3").value),
    parseFloat(document.getElementById("cota4").value),
    parseFloat(document.getElementById("cota5").value)
  ];

  const mizaTotala = parseFloat(document.getElementById("miza").value);

  if (cote.some(c => isNaN(c) || c <= 1) || isNaN(mizaTotala) || mizaTotala <= 0) {
    alert("Completează toate câmpurile corect (cote > 1, miza > 0).");
    return;
  }

  const sumaInversa = cote.reduce((sum, c) => sum + 1 / c, 0);
  const castigComun = mizaTotala / sumaInversa;

  let tableHTML = "<table><tr><th>Cotă</th><th>Miză optimă (RON)</th><th>Profit net (RON)</th></tr>";

  for (let i = 0; i < cote.length; i++) {
    const miza = castigComun / cote[i];
    const profit = castigComun - miza;
    tableHTML += `<tr>
        <td>${cote[i].toFixed(2)}</td>
        <td>${miza.toFixed(2)}</td>
        <td>${profit.toFixed(2)}</td>
      </tr>`;
  }

  tableHTML += "</table>";
  document.getElementById("rezultate").innerHTML = tableHTML;
  document.getElementById("castig").innerText = `Câștig brut comun: ${castigComun.toFixed(2)} RON`;
}
