package com.example.moretech

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.withStarted
import androidx.viewpager2.widget.ViewPager2
import com.example.moretech.adapters.MyFragmentAdapter
import com.example.moretech.datastore.DataStoreManager
import com.example.moretech.datastore.DataStoreManagerSingleton
import kotlinx.coroutines.launch


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        DataStoreManagerSingleton.dataStore = DataStoreManager(applicationContext)
        DataStoreManagerSingleton.token = ""
        lifecycleScope.launch {
            DataStoreManagerSingleton.token = DataStoreManagerSingleton.dataStore.getToken().toString()
        }
        setContentView(R.layout.activity_main)
        val viewPager: ViewPager2 = findViewById(R.id.pager)
        val adapter = MyFragmentAdapter(this)
        viewPager.adapter = adapter

    }



}