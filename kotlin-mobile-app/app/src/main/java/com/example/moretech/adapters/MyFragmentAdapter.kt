package com.example.moretech.adapters

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.example.moretech.FragmentLogin
import com.example.moretech.FragmentRegister

class MyFragmentAdapter(fragmentActivity: FragmentActivity) : FragmentStateAdapter(fragmentActivity) {
    override fun getItemCount(): Int = 2 // Number of fragments

    override fun createFragment(position: Int): Fragment {
        return when (position) {
            0 -> FragmentLogin()
            1 -> FragmentRegister()
            else -> throw IllegalArgumentException("Invalid position")
        }
    }
}