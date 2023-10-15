package com.example.moretech.viewmodels

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.moretech.models.CheckResponse
import com.example.moretech.models.RegisterResponse
import com.example.moretech.models.UserServiceApi
import com.example.moretech.models.LoginRequest
import com.example.moretech.models.LoginResponse
import kotlinx.coroutines.launch

class AuthViewModel(): ViewModel() {

    private val _tokenData = MutableLiveData<LoginResponse>()
    val tokenData: LiveData<LoginResponse> = _tokenData

    private val _checkToken = MutableLiveData<CheckResponse>()
    val checkToken: LiveData<CheckResponse> = _checkToken

    private val _idData = MutableLiveData<RegisterResponse>()
    val idData: LiveData<RegisterResponse> = _idData

    private val _error = MutableLiveData<String>()
    val error: LiveData<String> = _error

    init {

    }

    fun recieveToken(username: String, password: String) {
        viewModelScope.launch {
            try {
                val newToken = UserServiceApi.retrofitService.userLogin(LoginRequest(username,password))
                _tokenData.value = newToken
            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }

    fun checkToken(){
        viewModelScope.launch {
            try{
                val check = UserServiceApi.retrofitService.checkToken()
                _checkToken.value = check
            }catch (e: Exception){
                _checkToken.value = CheckResponse(false)
                _error.value = e.message
            }
        }
    }

    fun registerId(username: String, password: String){
        viewModelScope.launch {
            try {
                val newId = UserServiceApi.retrofitService.userRegister(LoginRequest(username,password))
                _idData.value = newId
            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }
}