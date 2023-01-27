// import Cookies from 'js-cookie';
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

axiosInstance.interceptors.response.use(
  (response) => response,
  (error) => {
    // Обработка ошибки
    if (error.response.status === 401) {
      console.log(error);
    } else {
      throw error;
    }
  }
);

async function POST(url, payload) {
  return await axiosInstance.post(url, payload, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });
}

async function GET(url) {
  return await axiosInstance.get(url, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });
}

// async function POST_WITH_TOKEN(url, payload) {
//   const token = `Bearer ${Cookies.get('accessToken')}`;

//   return await axiosInstance.post(url, payload, {
//     headers: {
//       Authorization: token,
//       Accept: 'application/json',
//     },
//   });
// }
// /* eslint-disable */
// async function GET_WITH_TOKEN(url, params) {
//   const token = `Bearer ${Cookies.get('accessToken')}`;

//   return await axiosInstance.get(url, {
//     headers: {
//       Authorization: token,
//       'Content-Type': 'application/json',
//       Accept: 'application/json',
//     },
//   });
// }
// /* eslint-enable */
// async function PATCH_WITH_TOKEN(url, payload) {
//   const token = `Bearer ${Cookies.get('accessToken')}`;

//   return await axiosInstance.patch(url, payload, {
//     headers: {
//       Authorization: token,
//       'Content-Type': 'application/json',
//       Accept: 'application/json',
//     },
//   });
// }

// async function PUT_WITH_TOKEN(url, payload) {
//   const token = `Bearer ${Cookies.get('accessToken')}`;

//   return await axiosInstance.put(url, payload, {
//     headers: {
//       Authorization: token,
//       'Content-Type': 'application/json',
//       Accept: 'application/json',
//     },
//   });
// }

// async function DELETE_WITH_TOKEN(url, payload) {
//   const token = `Bearer ${Cookies.get('accessToken')}`;

//   return await axiosInstance.delete(url, {
//     headers: {
//       Authorization: token,
//     },
//     data: payload,
//   });
// }
export { POST, GET };
//POST_WITH_TOKEN,
// GET_WITH_TOKEN,
// PATCH_WITH_TOKEN,
// PUT_WITH_TOKEN,
// DELETE_WITH_TOKEN,
