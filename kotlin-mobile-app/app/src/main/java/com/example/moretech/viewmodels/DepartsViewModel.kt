package com.example.moretech.viewmodels

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.moretech.models.AtmsModel
import com.example.moretech.models.CoordsModel
import com.example.moretech.models.FilterOfficeResponse
import com.example.moretech.models.LoginRequest
import com.example.moretech.models.LoginResponse
import com.example.moretech.models.OfficesModel
import com.example.moretech.models.RegisterResponse
import com.example.moretech.models.UserServiceApi
import kotlinx.coroutines.launch

class DepartsViewModel: ViewModel() {
    lateinit var updOfficeData: OfficesModel

    private val _atmData = MutableLiveData<AtmsModel>()
    val atmData: LiveData<AtmsModel> = _atmData

    var _officeData = MutableLiveData<OfficesModel>()
    var officeData: LiveData<OfficesModel> = _officeData

    private val _error = MutableLiveData<String>()
    val error: LiveData<String> = _error



    fun recieveDepartsInfo() {
        viewModelScope.launch {
            try {
                val newAtm = UserServiceApi.retrofitService.getAtms()
                _atmData.value = newAtm
            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }



    fun recieveOfficesInfo() {
        viewModelScope.launch {
            try {
                val newOffices = UserServiceApi.retrofitService.getOffices()

                updOfficeData = newOffices

                _officeData.value = newOffices

            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }


    fun updateOfficesInfo(settings: FilterOfficeResponse){
        viewModelScope.launch {
            try {
                val newOffices = UserServiceApi.retrofitService.sendFilter(settings)
                updOfficeData = newOffices
                _error.value = newOffices.offices.size.toString()
                _officeData.value = newOffices

            } catch (e: Exception) {
                _error.value = e.message
            }
        }
    }
}
