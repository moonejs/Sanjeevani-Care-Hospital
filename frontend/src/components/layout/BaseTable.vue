<template>
    <table class="table caption-top">
        <caption>
            <slot name="caption"/>
        </caption>
        <thead>
            <slot name="head"/>
        </thead>
        <tbody>
            <slot name="body" />
        </tbody>
        
        
    </table>
</template>