package com.example.moretech

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView

import com.example.moretech.databinding.InfoListItemBinding
import com.example.moretech.models.InfoCard


class ListViewAdapter: ListAdapter<InfoCard, ListViewAdapter.ListHolder>(ListComparator()){

    class ListHolder(private val binding: InfoListItemBinding) : RecyclerView.ViewHolder(binding.root){
        fun bind(infoCard: InfoCard) = with(binding){
            tvDepname.text = infoCard.name
            tvDepInfo.text = infoCard.info

        }
        companion object{
            fun create(parent: ViewGroup): ListHolder{
                return ListHolder(InfoListItemBinding.inflate(LayoutInflater.from(parent.context), parent, false))

            }
        }
    }

    class ListComparator : DiffUtil.ItemCallback<InfoCard>(){
        override fun areItemsTheSame(oldItem: InfoCard, newItem: InfoCard): Boolean {
            return oldItem == newItem
        }

        override fun areContentsTheSame(oldItem: InfoCard, newItem: InfoCard): Boolean {
            return oldItem == newItem
        }

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ListHolder {
        return ListHolder.create(parent)
    }

    override fun onBindViewHolder(holder: ListHolder, position: Int) {
        holder.bind(getItem(position))
    }

}