package com.example.moretech.datastore

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.withContext
import java.net.URLDecoder
import java.nio.charset.StandardCharsets

class DataStoreManager(context: Context) {

    private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "TOKEN")
    private val dataStore = context.dataStore

    companion object {
        val tokenKey = stringPreferencesKey("TOKEN_KEY")
    }

    val storedString: Flow<String?>
        get() = dataStore.data.map { preferences ->
            preferences[tokenKey]
        }

    suspend fun getToken(): String? {
        val decodedString = withContext(Dispatchers.IO) {
            URLDecoder.decode(storedString.first(), StandardCharsets.UTF_8.toString())
        }
        return decodedString
    }

    suspend fun clearDataStore() {
        dataStore.edit { preferences ->
            preferences.clear()
        }
    }

    suspend fun isDataStoreStringEmpty(): Boolean {
        val storedString = storedString.first()
        return storedString.isNullOrEmpty()
    }


    suspend fun storeString(value: String) {
        dataStore.edit { preferences ->
            preferences[tokenKey] = value
        }
    }
}