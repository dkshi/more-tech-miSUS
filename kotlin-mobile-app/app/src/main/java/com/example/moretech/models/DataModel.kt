package com.example.moretech.models


import com.example.moretech.datastore.DataStoreManagerSingleton
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import kotlinx.coroutines.runBlocking
import okhttp3.OkHttpClient
import okhttp3.Request
import retrofit2.Retrofit
import retrofit2.converter.moshi.MoshiConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import kotlin.coroutines.coroutineContext
import kotlin.coroutines.suspendCoroutine


private const val BASE_URL =
    "http://localhost:8080/"

private val moshi = Moshi.Builder()
    .add(KotlinJsonAdapterFactory())
    .build()



var client = OkHttpClient.Builder().addInterceptor { chain ->
    val newRequest: Request = chain.request().newBuilder()
        .addHeader("Authorization", "Bearer ${DataStoreManagerSingleton.token}")
        .build()
    chain.proceed(newRequest)
}.build()


val retrofit = Retrofit.Builder()
    .addConverterFactory(MoshiConverterFactory.create(moshi))
    .baseUrl(BASE_URL)
    .client(client)
    .build()

interface DataModelService{

    @GET("/check")
    suspend fun checkToken(): CheckResponse

    @GET("departments/atms")
    suspend fun getAtms(): AtmsModel

    @GET("departments/offices")
    suspend fun getOffices(): OfficesModel

    @POST("auth/sign-in")
    suspend fun userLogin(@Body loginRequest: LoginRequest): LoginResponse

    @POST("auth/sign-up")
    suspend fun userRegister(@Body loginRequest: LoginRequest): RegisterResponse

    @POST("departments/filter-offices")
    suspend fun sendFilter(@Body settings: FilterOfficeResponse): OfficesModel

}

object UserServiceApi{
    val retrofitService : DataModelService by lazy {
        retrofit.create(DataModelService::class.java) }
}

