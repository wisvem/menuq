const addProductFormBtn = document.querySelector("#add-product-form");
const submitFormBtn = document.querySelector('[type="submit"]');

const productForm = document.getElementsByClassName("product-form");
const mainForm = document.querySelector("#detail-form");

const totalForms = document.querySelector("[id$='-TOTAL_FORMS']");

let element = "";
if (totalForms.name.includes("product")) {
  element = "products";
} else {
  element = "menu_details";
}

// Total product forms
let formCount = productForm.length - 1;
// Create an empty form for new products forms
const emptyProductForm = productForm[formCount].cloneNode(true);

function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}

addProductFormBtn.addEventListener("click", function (event) {
  event.preventDefault();
  // Clone a new form

  const newProductForm = emptyProductForm.cloneNode(true);
  // regular expression to find all the matches and replace it with the updated form ID.
  const formRegex = RegExp(`(menu_details|products)-(\\d+){1}-`, 'g');
  newProductForm.innerHTML = newProductForm.innerHTML.replace(formRegex, `${element}-${formCount + 1}-`);
  // Insert new form before the last product form
  insertAfter(productForm[formCount], newProductForm);
  // increment formCount after add a new one
  formCount++;
  totalForms.setAttribute('value', `${formCount + 1}`);
});
