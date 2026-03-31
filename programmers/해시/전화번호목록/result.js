// function solution(phone_book) {
//   let count = 0;

//   for (const phone of phone_book) {
//     for (const book of phone_book) {
//       if (book.startsWith(phone)) count += 1;
//     }
//   }

//   return count > phone_book.length ? false : true;
// }

function solution(phone_book) {
  const phoneBook = new Set(phone_book);
  for (const phone of phone_book) {
    for (let i = 1; i <= phone.length; i++) {
      const text = phone.slice(0, i);
      if (phoneBook.has(text) && text !== phone) {
        return false;
      }
    }
  }

  return true;
}

// console.log(solution(["119", "97674223", "1195524421"]));
console.log(solution(["123", "456", "789"]));
