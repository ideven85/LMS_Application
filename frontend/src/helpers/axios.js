import axios  from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";

const axiosService = axios.create({
    baseURL: "http://localhost:8000/api",
    headers: {
        "Content-Type": "application/json"
    }
});

axiosService.interceptors.request.use(async (config)=>{
    /**
     * Retreiving the access token from local storage
     * and adding it to the headers
     */
    const {access} = JSON.parse(localStorage.getItem("auth"));
    config.headers.Authorization=`Bearer ${access}`;
    return config;
});

axiosService.interceptors.request.use(
    (req)=>Promise.resolve(req),
    (err)=>Promise.reject(err)
);

const refreshAuthLogic = async (failedRequest)=> {
    const {refresh} = JSON.parse(localStorage.getItem("auth"));

    return axios.post("/refresh/token",null,{
        baseURL: "localhost:8000/api",
        headers: {
            Authorization: `Bearer ${refresh}`

        },

    })
        .then((resp)=> {
            const {access, refresh} = resp.data;
            failedRequest.response.config.headers["Authorization"]="Bearer "+access;
            localStorage.setItem("auth",JSON.stringify({access,refresh}));
        })
        .catch(()=>{
            localStorage.removeItem("auth")
        });
};
createAuthRefreshInterceptor(axiosService,refreshAuthLogic);

export async function fetcher(url){
    return axiosService.get(url).then((res)=>res.data);
}
export default axiosService;


